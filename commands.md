# COMMANDS

## VQVAE

### Training
# bash scripts/train_objfeatvqvae.sh <tag> <gpu_id>
bash scripts/train_objfeatvqvae.sh threedfront_objfeat_vqvae 0

### Inference
# bash scripts/inference_objfeatvqvae.sh <tag> <gpu_id> <epoch>
bash scripts/inference_objfeatvqvae.sh threedfront_objfeat_vqvae 0 -1



---


## Layout Decoder
### Training
# bash scripts/train_sg2sc_objfeat.sh <room_type> <tag> <gpu_id> <fvqvae_tag>
bash scripts/train_sg2sc_objfeat.sh bedroom bedroom_sg2scdiffusion_objfeat 0 threedfront_objfeat_vqvae

### Inference
# bash scripts/inference_sg2sc_objfeat.sh <room_type> <tag> <gpu_id> <epoch> <fvqvae_tag> <(optional) cfg_scale>
bash scripts/inference_sg2sc_objfeat.sh bedroom bedroom_sg2scdiffusion_objfeat 0 -1 threedfront_objfeat_vqvae 1.0


---


## Semantic Graph Prior
### Training
# bash scripts/train_sg_vq_objfeat.sh <room_type> <tag> <gpu_id>
bash scripts/train_sg_vq_objfeat.sh bedroom bedroom_sgdiffusion_vq_objfeat 0

### Inference
# bash scripts/inference_sg_vq_objfeat.sh <room_type> <tag> <gpu_id> <epoch> <fvqvae_tag> <sg2sc_tag> <(optional) cfg_scale> <(optional) sg2sc_cfg_scale>
bash scripts/inference_sg_vq_objfeat.sh bedroom bedroom_sgdiffusion_vq_objfeat 0 -1 threedfront_objfeat_vqvae bedroom_sg2scdiffusion_objfeat 1.0 1.0

```
To visualize synthesized scenes, replace --n_scene 0 in scripts/inference_sg_vq_objfeat.sh to --n_scenes 5 --visualize --resolution 1024,
which means to visualize 5 synthesized scenes and save the rendered images with a resolution of 1024x1024.
Otherwise, it will only compute the iRecall score for evaluation.
```

---