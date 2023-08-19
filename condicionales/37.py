



Pamela = int(input( "Pamela : ") )
Karol = int(input( "Karol : ") )
Fany = int(input( "Fany : ") )

mitad = ( Pamela + Karol + Fany ) // 2

mensaje = ""
if Pamela > mitad  : mensaje ="Gano Pamela"
elif Karol > mitad : mensaje = "Gano Karol"
elif Fany > mitad : mensaje = "Gano Fany"

elif Pamela < Karol and Pamela < Fany : mensaje 