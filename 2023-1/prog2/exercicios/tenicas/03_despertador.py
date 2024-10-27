def alarme(hora_atual, minuto_atual, hora_alarme, minuto_alarme):
	t1 = hora_atual*60 + minuto_atual
	t2 = hora_alarme*60 + minuto_alarme
    
	if (t1 < t2):
		# Dorme e acorda no mesmo dia:
		print(t2-t1)
	else:
		# Dorme e acorda em dias diferentes
		print (24*60 + t2-t1)