export type MetricRow = {
  series: string;
  latest: number | string;
  previous?: number | string;
  consensus?: number | string;
  surprise?: number | string;
  trend?: string;
  regime_signal?: string;
  market_impact?: string;
  last_updated: string;
  delayed?: boolean;
};

export type TabPayload = { tab: string; rows: MetricRow[] };
