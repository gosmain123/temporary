from app.parsers.sec_13f import parse_13f_information_table


def test_parse_13f_xml() -> None:
    xml = """
    <informationTable>
      <infoTable>
        <nameOfIssuer>APPLE INC</nameOfIssuer>
        <cusip>037833100</cusip>
        <value>1000</value>
        <shrsOrPrnAmt><sshPrnamt>5000</sshPrnamt></shrsOrPrnAmt>
      </infoTable>
    </informationTable>
    """
    holdings = parse_13f_information_table(xml)
    assert len(holdings) == 1
    assert holdings[0].issuer == "APPLE INC"
    assert holdings[0].cusip == "037833100"
