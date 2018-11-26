def color_hash_from_name(name):
	h = 0
	ch = ord(name[0])
	for i in name:
		h = h * 31 + ch
	color_hash = h % 0xffffff
	if color_hash < 0x100000:
		color_hash += 0x100000
	return f"#{format(color_hash, 'x')}"
