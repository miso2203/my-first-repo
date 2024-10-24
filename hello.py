def print_hello(value: str) -> str:
	if isinstance(value, str):
		return print(f'hello, {value}')
	else:
		return 'This is not string.'


if __name__ == '__main__':
	print_hello('John')
