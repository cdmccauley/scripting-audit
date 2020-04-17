# demonstrates: list, variable declaration, variable assignment
# declarations
$choices = 
    "rock",
    "paper",
    "scissors",
    "lizard",
    "Spock"

$playAgain = "y"

# demonstrate: Write-Host, literal, escape character
# print header
Write-Host "**** Welcome to Rock, Paper, Scissors ****`n"

# demonstrates: while loop, comparison
# start game
while ($playAgain -eq "y") {
    # demonstrates: pipe, Get-Random
    # get computer choice
    $computer = $choices | Get-Random

    # demonstrates: Read-Host, -contains, Write-Warning
    # get player input
    $inputOk = $false
    while ($inputOk -eq $false) {
        $player1 = Read-Host "Player 1, choose rock, paper, scissors, lizard, or spock"
        if ($choices -contains $player1) {
            $inputOk = $true
        } else {
            Write-Warning -Message "Error: invalid selection. Try again."
        }
    }

    # demonstrates: if, elseif, -and
    # determine game outcome
    if ($player1 -eq $computer) {
        Write-Host "Tie, both players chose $computer"
    } elseif ($player1 -eq "rock" -and $computer -eq "paper") {
        Write-Host "The computer wins, paper covers rock."
    } elseif ($player1 -eq "rock" -and $computer -eq "scissors") {
        Write-Host "Player 1 wins, rock smashes scissors."
    } elseif ($player1 -eq "rock" -and $computer -eq "lizard") {
        Write-Host "Player 1 wins, rock smashes lizard"
    } elseif ($player1 -eq "rock" -and $computer -eq "spock") {
        Write-Host "The computer wins, Spock vaporizes rock."
    } elseif ($player1 -eq "paper" -and $computer -eq "rock") {
        Write-Host "Player 1 wins, paper covers rock."
    } elseif ($player1 -eq "paper" -and $computer -eq "scissors") {
        Write-Host "The computer wins, scissors cut paper."
    } elseif ($player1 -eq "paper" -and $computer -eq "lizard") {
        Write-Host "The computer wins, lizard eats paper."
    } elseif ($player1 -eq "paper" -and $computer -eq "spock") {
        Write-Host "Player 1 wins, paper disproves Spock"
    } elseif ($player1 -eq "scissors" -and $computer -eq "rock") {
        Write-Host "The computer wins, rock smashes scissors."
    } elseif ($player1 -eq "scissors" -and $computer -eq "paper") {
        Write-Host "Player 1 wins, scissors cut paper."
    } elseif ($player1 -eq "scissors" -and $computer -eq "lizard") {
        Write-Host "Player 1 wins, scissors decapitate lizard."
    } elseif ($player1 -eq "scissors" -and $computer -eq "spock") {
        Write-Host "The computer wins, Spock smashes scissors."
    } elseif ($player1 -eq "lizard" -and $computer -eq "rock") {
        Write-Host "The computer wins, rock smashes lizard."
    } elseif ($player1 -eq "lizard" -and $computer -eq "paper") {
        Write-Host "Player 1 wins, lizard eats paper."
    } elseif ($player1 -eq "lizard" -and $computer -eq "scissors") {
        Write-Host "The computer wins, scissors decapitate lizard."
    } elseif ($player1 -eq "lizard" -and $computer -eq "spock") {
        Write-Host "Player 1 wins, lizard poisons Spock."
    } elseif ($player1 -eq "spock" -and $computer -eq "rock") {
        Write-Host "Player 1 wins, Spock vaporizes rock."
    } elseif ($player1 -eq "spock" -and $computer -eq "paper") {
        Write-Host "The computer wins, paper disproves Spock."
    } elseif ($player1 -eq "spock" -and $computer -eq "scissors") {
        Write-Host "Player 1 wins, Spock smashes scissors."
    } elseif ($player1 -eq "spock" -and $computer -eq "lizard") {
        Write-Host "The computer wins, lizard poisons Spock."
    }

    # prompt for continuation or termination
    $playAgain = Read-Host "Enter 'Y' to play again"
    
}