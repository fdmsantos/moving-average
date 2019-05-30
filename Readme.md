# Deploy

## Docker

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/
docker build -t moving_average .
docker run --rm -v $(pwd)/data:/data moving_average -i /data/events.json -w 10
```

# Run Tests

```bash
git clone https://github.com/fdmsantos/moving-average
cd moving-average/
python test_calculate_cli.py
```