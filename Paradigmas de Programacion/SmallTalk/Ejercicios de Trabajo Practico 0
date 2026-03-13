" 7507/9502 | TP0: Trabajo Práctico 0 | Enunciado "

| error pelisRankings pelicula1 pelicula2 pelicula3 pelicula4 pelicula5 pelicula6 peliculaMasLarga calificacion mejorPelicula |

Transcript clear.
error := false.

pelisRankings := PelisRankings new.

pelicula1 := Pelicula new.
pelicula1 establecerNombre: '2001: Odisea del espacio'.
pelicula1 establecerDuracionEnMinutos: 143.
pelicula1 establecerAnio: 1968.
pelisRankings agregarPelicula: pelicula1.

pelicula2 := Pelicula new.
pelicula2 establecerNombre: 'El planeta de los simios'.
pelicula2 establecerDuracionEnMinutos: 112.
pelicula2 establecerAnio: 1968.
pelisRankings agregarPelicula: pelicula2.

pelicula3 := Pelicula new.
pelicula3 establecerNombre: 'El Imperio contraataca'.
pelicula3 establecerDuracionEnMinutos: 124.
pelicula3 establecerAnio: 1980.
pelisRankings agregarPelicula: pelicula3.

pelicula4 := Pelicula new.
pelicula4 establecerNombre: 'Viernes 13'.
pelicula4 establecerDuracionEnMinutos: 95.
pelicula4 establecerAnio: 1980.
pelisRankings agregarPelicula: pelicula4.

pelicula5 := Pelicula new.
pelicula5 establecerNombre: 'Forrest Gump'.
pelicula5 establecerDuracionEnMinutos: 142.
pelicula5 establecerAnio: 1994.
pelisRankings agregarPelicula: pelicula5.

peliculaMasLarga := pelisRankings peliculaMasLarga.
(peliculaMasLarga = '2001: Odisea del espacio') ifFalse: [
  Transcript show: 'Error. La película más larga es 2001: Odisea del espacio.' ; cr.
  error := true.
].

pelicula6 := Pelicula new.
pelicula6 establecerNombre: 'Tiempos violentos'.
pelicula6 establecerDuracionEnMinutos: 154.
pelicula6 establecerAnio: 1994.
pelisRankings agregarPelicula: pelicula6.

peliculaMasLarga := pelisRankings peliculaMasLarga.
(peliculaMasLarga = 'Tiempos violentos') ifFalse: [
  Transcript show: 'Error. La película más larga es Tiempos violentos.' ; cr.
  error := true.
].

pelisRankings calificarPelicula: 'Tiempos violentos' conPuntaje: 8.
pelisRankings calificarPelicula: '2001: Odisea del espacio' conPuntaje: 9.
pelisRankings calificarPelicula: 'Forrest Gump' conPuntaje: 4.
pelisRankings calificarPelicula: 'Viernes 13' conPuntaje: 2.
pelisRankings calificarPelicula: 'Tiempos violentos' conPuntaje: 10.
pelisRankings calificarPelicula: 'Viernes 13' conPuntaje: 6.
pelisRankings calificarPelicula: 'El planeta de los simios' conPuntaje: 8.
pelisRankings calificarPelicula: 'El Imperio contraataca' conPuntaje: 10.
pelisRankings calificarPelicula: 'Forrest Gump' conPuntaje: 6.
pelisRankings calificarPelicula: 'El planeta de los simios' conPuntaje: 6.

calificacion := pelisRankings obtenerPuntajePromedioDe: 'Tiempos violentos'.
(calificacion closeTo: 9) ifFalse: [
  Transcript show: 'Error. El puntaje promedio de Tiempos Violentos es 9'; cr.
  error := true.
].

calificacion := pelisRankings obtenerPuntajePromedioDe: '2001: Odisea del espacio'.
(calificacion closeTo: 9) ifFalse: [
  Transcript show: 'Error. El puntaje promedio de 2001: Odisea del espacio es 9'; cr.
  error := true.
].

calificacion := pelisRankings obtenerPuntajePromedioDe: 'Viernes 13'.
(calificacion closeTo: 4) ifFalse: [
  Transcript show: 'Error. El puntaje promedio de Viernes 13 es 4'; cr.
  error := true.
].

calificacion := pelisRankings obtenerPuntajePromedioDe: 'Forrest Gump'.
(calificacion closeTo: 5) ifFalse: [
  Transcript show: 'Error. El puntaje promedio de Forrest Gump es 5'; cr.
  error := true.
].

calificacion := pelisRankings obtenerPuntajePromedioDe: 'El Imperio contraataca'.
(calificacion closeTo: 10) ifFalse: [
  Transcript show: 'Error. El puntaje promedio de El Imperio contraataca es 10'; cr.
  error := true.
].

calificacion := pelisRankings obtenerPuntajePromedioDe: 'El planeta de los simios'.
(calificacion closeTo: 7) ifFalse: [
  Transcript show: 'Error. El puntaje promedio de El planeta de los simios es 7'; cr.
  error := true.
].

mejorPelicula := pelisRankings mejorPeliculaDelAnio: 1980.
(mejorPelicula = 'El Imperio contraataca') ifFalse: [
  Transcript show: 'Error. La mejor película del año 1980 es El Imperio contraataca'; cr.
  error := true.
].

mejorPelicula := pelisRankings mejorPeliculaDelAnio: 1968.
(mejorPelicula = '2001: Odisea del espacio') ifFalse: [
  Transcript show: 'Error. La mejor película del año 1968 es 2001: Odisea del espacio'; cr.
  error := true.
].

mejorPelicula := pelisRankings mejorPeliculaDelAnio: 1994.
(mejorPelicula = 'Tiempos violentos') ifFalse: [
  Transcript show: 'Error. La mejor película del año 1994 es Tiempos violentos'; cr.
  error := true.
].

mejorPelicula := pelisRankings mejorPeliculaDeTodosLosTiempos.
(mejorPelicula = 'El Imperio contraataca') ifFalse: [
  Transcript show: 'Error. La mejor película de todos los tiempos es El Imperio contraataca'; cr.
  error := true.
].

" Resultado final. "
error ifTrue: [
	Transcript show: 'Resultado final: ERROR'.
]
ifFalse: [
	Transcript show: 'Resultado final: OK'.
].
