run:
	docker-compose down
	docker-compose up --build --detach

debug:
	docker-compose down
	docker-compose up --build --detach
	docker logs receiver --follow
