# Domain Events (Draft)

## Naming

`<bounded_context>.<entity>.<action>`

Örnekler:
- `catalog.product.created`
- `order.order.created`
- `payment.invoice.paid`
- `logistics.shipment.delayed`

## Event Envelope

```json
{
  "event_id": "uuid",
  "event_name": "order.order.created",
  "occurred_at": "2026-04-29T12:00:00Z",
  "tenant_id": "acme",
  "actor": {
    "type": "user|agent|system",
    "id": "string"
  },
  "payload": {},
  "metadata": {
    "correlation_id": "uuid",
    "causation_id": "uuid"
  }
}
```

## Policy Hooks

- Hassas işlem eventleri (`payment.*`, `compliance.*`) için zorunlu audit.
- Toplu değişiklik eventleri için insan onayı gerekliliği.

