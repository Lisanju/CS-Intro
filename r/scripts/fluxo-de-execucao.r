# Controle do fluxo de execução do programa

if(TRUE) message("It was true!")

if(FALSE) message("It wasn't true!")

if(runif(1) > 0.5) message("This message appears with a 50% chance.")

repeat
{
    message("Happy Groundhog Day!")
    action <- sample(
        c(
            "Learn French",
            "Make an ice statue",
            "Rob a bank",
            "Win heart of Andie McDowell"
        ),
        1
    )
    message("action = ", action)
    if(action == "Win heart of Andie McDowell") break
}

action <- sample(
    c(
        "Learn French",
        "Make an ice statue",
        "Rob a bank",
        "Win heart of Andie McDowell"
    ),
    1
)

while(action != "Win heart of Andie McDowell")
{
    message("Happy Groundhog Day!")
    action <- sample(
        c(
            "Learn French",
            "Make an ice statue",
            "Rob a bank",
            "Win heart of Andie McDowell"
        ),
        1
    )
    message("action = ", action)
}

for(i in 1:5) message("i = ", i)

for(i in 1:5)
{
    j <- i ^ 2
    message("j = ", j)
}

for(month in month.name) {
    message("The month of ", month)
}
