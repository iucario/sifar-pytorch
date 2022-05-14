 python main.py --data_dir ucf101 --dataset ucf101 \
 --opt adamw --lr 1e-4 --epochs 5 --sched cosine --duration 8 \
 --batch-size 2 --super_img_rows 3 --disable_scaleup \
 --mixup 0.8 --cutmix 1.0 --drop-path 0.1 --pretrained \
 --warmup-epochs 5 --no-amp --model sifar_base_patch4_window14_224_3x3 \
 --output_dir output