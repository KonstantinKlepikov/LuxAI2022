fit:
	cd src/engine && python train.py --n-envs 10 --log-path logs/fit/exp_$(DEST) --seed ${SEED}

board:
	cd src/engine && tensorboard --logdir logs

play:
	luxai-s2 src/engine/main.py src/engine/main.py --out=src/engine/replays/replay_`date +'%y.%m.%d_%H:%M'`.json

replay:
	luxai-s2 src/engine/main.py src/engine/main.py -v 2 -s 101 -o src/engine/replays/replay_`date +'%y.%m.%d_%H:%M'`.html

submission:
	cd src/engine && sh make_sub.sh

submit:
	kaggle competitions submit -c lux-ai-season-2 -f src/engine/submissions/submission.tar.gz -m "submission"