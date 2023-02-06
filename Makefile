play:
	luxai-s2 src/engine/main.py src/engine/main.py --out=src/engine/replays/replay.json

replay:
	luxai-s2 src/engine/main.py src/engine/main.py -v 2 -s 101 -o src/engine/replays/replay.html

submission:
	cd src/engine && sh make_sub.sh

submit:
	kaggle competitions submit -c lux-ai-season-2 -f src/engine/submissions/submission.tar.gz -m "submission"