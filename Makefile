##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## Makefile
##

NAME	=	groundhog

$(NAME)	:
			cp src/main.py ./
			mv main.py groundhog
			chmod +x groundhog

all	:	$(NAME)

clean:
		rm -rf groundhog src/__pycache__ __pycache__

fclean:	clean

re	:	fclean all

.PHONY: all clean fclean re
