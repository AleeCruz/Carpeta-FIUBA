TestCase subclass: #AlgoTekTest	instanceVariableNames: 'precision'	classVariableNames: ''	package: 'TP1-Tests'!!AlgoTekTest methodsFor: 'tests' stamp: 'Joaquin 9/13/2023 20:51'!test07SacarUnaEntradaPagandoConTarjetaTieneUnDescuento	
	| costoAPagar costoEsperado ubicacionElegida algoTek evento tarjeta |
	
	"Arrange"
	evento := 'The Eras Tour, en River'.
	algoTek := AlgoTek registrarEvento: evento deArtistaInternacional: 'Taylor Swift' conTarifaArtista: 100000.

	ubicacionElegida := 'M912'.
	tarjeta := Tarjeta conNombre: 'Patagonia'.	
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: ubicacionElegida tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'D018' tarifa: 20000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Delantero' tarifa: 75000. "ay amiga, + sErVIcE CHanGe"
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Trasero' tarifa: 40000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Karma is my Boyfriend' tarifa: 155000 lugaresDisponibles: 2.
	algoTek paraEvento: evento registrarUbicacionViP: 'Its a Love Story' tarifa: 85000 lugaresDisponibles: 2.


	"Al ser un artista internacional, el impuesto 'al disfrute' te vacuna"
	costoEsperado := (100000 * 2) / 5 + 1000.
	
	"Al ser platea, se sacan los dos ultimos numeros de la ubicacion y se multiplica por la tarifa de platea"
	costoEsperado := costoEsperado + (12 * 25000).

	"Al pagar con tarjeta Patagonia, hay descuento del 20%"
	costoEsperado := costoEsperado * 0.8.

	"Act"	
	costoAPagar := algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: tarjeta.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !!AlgoTekTest methodsFor: 'tests' stamp: 'Joaquin 9/13/2023 20:51'!test04SacarUnaEntradaParaUnArtistaInternacionalEnPlateaPoseeElSiguienteCosto	
	| costoAPagar costoEsperado ubicacionElegida algoTek evento efectivo |
	
	"Arrange"
	evento := 'The Eras Tour, en River'.	efectivo := Efectivo new.
	algoTek := AlgoTek registrarEvento: evento deArtistaInternacional: 'Taylor Swift' conTarifaArtista: 100000.

	ubicacionElegida := 'M912'.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: ubicacionElegida tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'D018' tarifa: 20000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Delantero' tarifa: 75000. "ay amiga, + sErVIcE CHanGe"
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Trasero' tarifa: 40000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Karma is my Boyfriend' tarifa: 155000 lugaresDisponibles: 2.
	algoTek paraEvento: evento registrarUbicacionViP: 'Its a Love Story' tarifa: 85000 lugaresDisponibles: 2.


	"Al ser un artista internacional, el impuesto 'al disfrute' te vacuna"
	costoEsperado := (100000 * 2) / 5 + 1000.
	
	"Al ser platea, se sacan los dos ultimos numeros de la ubicacion y se multiplica por la tarifa de platea"
	costoEsperado := costoEsperado + (12 * 25000).

	"Act"	
	costoAPagar := algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: efectivo.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !!AlgoTekTest methodsFor: 'tests' stamp: 'Joaquin 9/13/2023 20:49'!test01SacarUnaEntradaParaUnArtistaEnUnaUbicacionEnParticularPoseeElSiguienteCosto	
	| costoAPagar costoEsperado ubicacionElegida algoTek evento efectivo |
	
	"Arrange"
	evento := 'La Ultima Noche Magica En River'.	efectivo := Efectivo new.
	algoTek := AlgoTek registrarEvento: evento deArtistaNacional: 'Tan Bionica' conTarifaArtista: 50000.

	ubicacionElegida := 'D018'.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'M912' tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: ubicacionElegida tarifa: 2000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo General' tarifa: 16000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Hospitality' tarifa: 40000 lugaresDisponibles: 2.
	
	"Al ser un artista nacional, se subsidia su tarifa de artista"
	costoEsperado := 50000 log.
	
	"Al ser platea, se sacan los dos ultimos numeros de la ubicacion y se multiplica por la tarifa de platea"
	costoEsperado := costoEsperado + (18 * 2000).

	"Act"	
	costoAPagar := algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: efectivo.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !!AlgoTekTest methodsFor: 'tests' stamp: 'Joaquin 9/13/2023 20:50'!test02SacarUnaEntradaParaUnArtistaNacionalEnCampoPoseeElSiguienteCosto	
	| costoAPagar costoEsperado ubicacionElegida algoTek evento efectivo |
	
	"Arrange"
	evento := 'La Ultima Noche Magica En River'.	efectivo := Efectivo new.
	algoTek := AlgoTek registrarEvento: evento deArtistaNacional: 'Tan Bionica' conTarifaArtista: 50000.

	ubicacionElegida := 'Campo General'.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'M912' tarifa: 2000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'D018' tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo General' tarifa: 16000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Hospitality' tarifa: 40000 lugaresDisponibles: 2.
	
	"Al ser un artista nacional, se subsidia su tarifa de artista"
	costoEsperado := 50000 log.
	
	"Al ser campo, el costo es fijo"
	costoEsperado := costoEsperado + 16000.

	"Act"	
	costoAPagar := algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: efectivo.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !!AlgoTekTest methodsFor: 'tests' stamp: 'Joaquin 9/13/2023 20:51'!test03SacarUnaEntradaParaUnArtistaNacionalEnViPPoseeElSiguienteCosto	
	| costoAPagar costoEsperado ubicacionElegida algoTek evento efectivo |
	
	"Arrange"
	evento := 'La Ultima Noche Magica En River'.	efectivo := Efectivo new.
	algoTek := AlgoTek registrarEvento: evento deArtistaNacional: 'Tan Bionica' conTarifaArtista: 50000.

	ubicacionElegida := 'Hospitality'.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'M912' tarifa: 2000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'D018' tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo General' tarifa:  16000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Hospitality' tarifa:  40000 lugaresDisponibles: 10.
	
	"Al ser un artista nacional, se subsidia su tarifa de artista"
	costoEsperado := 50000 log.
	
	"Al ser Hospitality, la tarifa se va encareciendo a medida que se van ocupando los lugares"
	costoEsperado := costoEsperado + (40000 / 10).

	"Act"	
	costoAPagar := algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: efectivo.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !!AlgoTekTest methodsFor: 'tests' stamp: 'Joaquin 9/13/2023 20:52'!test05LaEntradaMasBarataParaUnArtistaInternacionalPoseeElSiguienteCosto	
	| costoAPagar costoEsperado algoTek evento efectivo |
	
	"Arrange"
	evento := 'The Eras Tour, en River'.	efectivo := Efectivo new.
	algoTek := AlgoTek registrarEvento: evento deArtistaInternacional: 'Taylor Swift' conTarifaArtista: 100000.

	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'M912' tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'D018' tarifa: 20000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Delantero' tarifa: 75000. "ay amiga, + sErVIcE CHanGe"
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Trasero' tarifa: 40000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Karma is my Boyfriend' tarifa: 155000 lugaresDisponibles: 2.
	algoTek paraEvento: evento registrarUbicacionViP: 'Its a Love Story' tarifa: 85000 lugaresDisponibles: 2.


	"Al ser un artista internacional, el impuesto 'al disfrute' te vacuna"
	costoEsperado := (100000 * 2) / 5 + 1000.
	
	"La entrada mas barata pertenece a la ubicacion de campo trasero en este caso"
	costoEsperado := costoEsperado + 40000.

	"Act"	
	costoAPagar := algoTek entradaMasBarataPara: evento pagandoCon: efectivo.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !!AlgoTekTest methodsFor: 'tests' stamp: 'AV 9/18/2023 20:08'!test06SacarUnaEntradaParaUnArtistaInternacionalEnViPVaAumentandoSegunLocalidadesDisponibles	
	| costoAPagar costoEsperado ubicacionElegida algoTek evento efectivo |
	
	"Arrange"
	evento := 'The Eras Tour, en River'.	efectivo := Efectivo new.
	algoTek := AlgoTek registrarEvento: evento deArtistaInternacional: 'Taylor Swift' conTarifaArtista: 100000.

	ubicacionElegida := 'Its a Love Story'.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'A011' tarifa: 25000.
	algoTek paraEvento: evento registrarUbicacionPlateaPreferencial: 'D018' tarifa: 20000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Delantero' tarifa: 75000.
	algoTek paraEvento: evento registrarUbicacionCampo: 'Campo Trasero' tarifa: 40000.
	algoTek paraEvento: evento registrarUbicacionViP: 'Karma is my Boyfriend' tarifa: 155000 lugaresDisponibles: 2.
	algoTek paraEvento: evento registrarUbicacionViP: 'Its a Love Story' tarifa: 85000 lugaresDisponibles: 2.

	"Ya se saco esta el 'Its a Love Story', por lo tanto se reduce el lugar disponible"
	algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: efectivo.

	"Al ser un artista internacional, el impuesto 'al disfrute'"
	costoEsperado := (100000 * 2) / 5 + 1000.
	
	"Al ser 'Its a Love Story', la tarifa se va encareciendo a medida que se van ocupando los lugares"
	costoEsperado := costoEsperado + (85000 / 1).

	"Act"	
	costoAPagar := algoTek costoEntradaPara: evento enUbicacion: ubicacionElegida pagandoCon: efectivo.
	
	"Assert"
	self assert: costoAPagar closeTo: costoEsperado precision: 0.0001 ! !