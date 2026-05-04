# Agent Catalog (MVP)

| Agent | Sorumluluk | Trigger |
|---|---|---|
| OrderOpsAgent | Sipariş yaşam döngüsü yönetimi | `order.created`, `order.updated` |
| InventoryGuardAgent | Stok düşüş/risk kontrolü | `inventory.changed` |
| PaymentReconcileAgent | Ödeme mutabakatı | `payment.settled`, `payment.failed` |
| LogisticsAgent | Kargo/teslimat orchestration | `shipment.created`, `shipment.delayed` |
| CustomerCareAgent | Müşteri iletişim ve SLA takibi | `ticket.opened`, `ticket.escalated` |
| MarketingContentAgent | Kampanya/içerik üretimi | `campaign.requested` |
| ComplianceAgent | KVKK/GDPR policy denetimi | Tüm hassas eventler |
| IncidentAgent | Kritik durum alarm/escalation | `incident.critical` |

