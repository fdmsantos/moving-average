# Deploy

## Docker

```bash
docker build -t translator .
docker run --rm -v $(pwd)/data:/data translator -i /data/events.json -w 10
```