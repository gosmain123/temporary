import type { TabPayload } from "./types";

export const fallbackControlTower: TabPayload = {
  tab: "control_tower",
  rows: [
    { series: "Core CPI MoM", latest: 0.3, previous: 0.2, consensus: 0.2, surprise: 0.1, trend: "sticky", regime_signal: "inflation risk", market_impact: "bearish duration", last_updated: new Date().toISOString() },
    { series: "NFP", latest: "184k", previous: "162k", consensus: "170k", surprise: "+14k", trend: "resilient", regime_signal: "risk-on", market_impact: "supports cyclicals", last_updated: new Date().toISOString() }
  ]
};

export const tabs = [
  "Control Tower",
  "Economic Calendar",
  "Inflation",
  "Labor",
  "Growth / Activity",
  "PMI / Surveys",
  "Housing",
  "Fed / Policy / Liquidity",
  "Rates / FX / Cross-Asset",
  "Positioning / Flows",
  "13F / Ownership / Crowding",
  "Treasury / Funding / Auctions",
  "Playbook / Scenarios"
];
