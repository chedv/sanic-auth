from sanic import response
from http import HTTPStatus

unauthorized = response.json({'message': HTTPStatus.UNAUTHORIZED.phrase}, status=HTTPStatus.UNAUTHORIZED)
