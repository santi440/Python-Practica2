def builder(names,goals,goals_avoided,assists):
    """Generar una dicionario con los nombres como clave y un diccionario con todas las estadísticas asociadas a cada jugador(goles,goles evitados y asistencia)"""
    stats = {}
    for name, goals_scored, goals_avoided, assists_count in zip(names.split(', '), goals, goals_avoided, assists):
        stats[name] = {'Goles a favor': goals_scored, 'Goles evitados': goals_avoided, 'Asistencias': assists_count}
    return stats

def goald_leader_goals(stats):
    """Recibe un diccionario con jugadores cargados y devuelve maximo goleador o goleadora del equipo.
    Retorna el nombre y la cantidad de goles del goleador o goleadora como tupla(nombre,goles)"""
    goald_leader = max(stats, key=lambda x: stats[x]['Goles a favor'])
    return goald_leader,stats[goald_leader]["Goles a favor"]

def influence(stats):
    """Recibe un diccionario con jugadores cargados y devuelve el jugador o jugadora más influyente de la temporada."""
    return max(stats, key=lambda x: stats[x]['Goles a favor']*1.5 + stats[x]['Goles evitados']*1.25 + stats[x]['Asistencias'])

def influence2(stats):
    result = map(lambda x:(x,stats[x]['Goles a favor']*1.5 + stats[x]['Goles evitados']*1.25 + stats[x]['Asistencias']),stats)
    result = tuple(result)
    most_influential = max(result,key= lambda x: x[1])
    return most_influential[0]

def team_average(stats):
    """Calcula el promedio de goles por partido del equipo en general sobre un iterable"""
    total_goals = sum(stats[x]['Goles a favor']for x in stats)
    return total_goals / 25

def goald_leader_average(stats):
    """Recibe un diccionario con jugadores cargados y devuelve el promedio de goles por partido del goleador o goleadora"""
    return goald_leader_goals(stats)[1] / 25

