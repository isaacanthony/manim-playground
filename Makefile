run:
	@docker run \
		--name manim \
		--env PYTHONDONTWRITEBYTECODE=1 \
		--rm \
		--volume $(PWD)/data:/data \
		--volume $(PWD)/src:/src \
		-it \
		manimcommunity/manim:v0.8.0 manim -o /data/square_to_circle.mp4 /src/square_to_circle.py SquareToCircle
