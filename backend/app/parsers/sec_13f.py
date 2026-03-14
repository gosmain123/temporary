from dataclasses import dataclass
from xml.etree import ElementTree as ET


@dataclass
class Holding:
    issuer: str
    cusip: str
    value: int
    shares: int


def parse_13f_information_table(xml_text: str) -> list[Holding]:
    root = ET.fromstring(xml_text)
    ns = {"n": root.tag.split("}")[0].strip("{")} if "}" in root.tag else {}

    def q(tag: str) -> str:
        return f"n:{tag}" if ns else tag

    results: list[Holding] = []
    for info in root.findall(q("infoTable"), ns):
        issuer = (info.findtext(q("nameOfIssuer"), default="", namespaces=ns) or "").strip()
        cusip = (info.findtext(q("cusip"), default="", namespaces=ns) or "").strip()
        value = int((info.findtext(q("value"), default="0", namespaces=ns) or "0").strip())
        shares = int((info.find(q("shrsOrPrnAmt"), ns).findtext(q("sshPrnamt"), default="0", namespaces=ns) or "0").strip())
        results.append(Holding(issuer=issuer, cusip=cusip, value=value, shares=shares))
    return results
