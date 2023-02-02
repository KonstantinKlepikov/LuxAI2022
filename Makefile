play:
	luxai-s2 src/engine/main.py src/engine/main.py --out=src/output/replay.json

replay:
	luxai-s2 src/engine/main.py src/engine/main.py -v 2 -s 101 -o src/output/replay.html

submit:
	kaggle competitions submit -c lux-ai-season-2 -f src/output/submission.tar.gz -m "submission"