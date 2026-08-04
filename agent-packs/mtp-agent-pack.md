# MTP Speculative Decoding Agent Pack

When deploying or tuning speculative decoding, load this agent pack:

## Pre-flight
- Read `doctrines/MTP-SPECULATIVE-DECODING.md`
- Read `intake/mtp-speculative-decoding-intake.md`
- Check acceptance rate: `curl localhost:8000/metrics | grep spec_decode`
- Run acceptance calculator: `python3 scripts/acceptance-calculator.py`

## Core commands
```bash
# Run acceptance calculator
python3 /Users/mikerodgers/Developer/RIGForge/repos/mtp-inference-studio/scripts/acceptance-calculator.py

# Deploy with draft model (vLLM)
docker run --gpus all --ipc=host -p 8000:8000 \
  -e HUGGING_FACE_HUB_TOKEN=$HF_TOKEN \
  vllm/vllm-openai:latest \
  --model meta-llama/Llama-3.3-70B-Instruct --quantization fp8 \
  --speculative-model meta-llama/Llama-3.2-1B-Instruct \
  --num-speculative-tokens 5

# Check fleet nodes
bash /Users/mikerodgers/Developer/RIGForge/repos/mtp-inference-studio/scripts/deploy-fleet.sh
```

## When NOT to use
- batch > 32 → standard decoding
- output tokens < 50 → standard decoding
- alpha < 0.50 → disable or switch drafter
- embeddings or classifiers → never enable