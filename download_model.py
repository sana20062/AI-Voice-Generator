from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="coqui/XTTS-v2",
    local_dir="xtts_model"
)

print("Model downloaded")