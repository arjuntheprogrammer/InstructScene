from huggingface_hub import HfApi

api = HfApi()
api.upload_file(
    path_or_fileobj="/home/cto_auraml_com/Development/InstructScene/out/bedroom_sg2scdiffusion_objfeat/checkpoints/epoch_01999.pth",
    path_in_repo="bedroom_sg2scdiffusion_objfeat_epoch_01999.pth",
    repo_id="chenguolin/InstructScene_dataset",
    commit_message="Upload bedroom_sg2scdiffusion_objfeat_epoch_01999.pth"
)