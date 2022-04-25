const tileDisplay = document.querySelector('.tile-container')
const messageDisplay = document.querySelector('.message-container')

const wordle = 'SUPER'

const guessRows = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
]
let currentRow = 0
let currentTile = 0
let isGameOver = false

guessRows.forEach((guessRow, guessRowIndex) => {
    const rowElement = document.createElement('div')
    rowElement.setAttribute('id', 'guessRow-' + guessRowIndex)
    guessRow.forEach((_guess, guessIndex) => {
        const tileElement = document.createElement('div')
        tileElement.setAttribute('id', 'guessRow-' + guessRowIndex + '-tile-' + guessIndex)
        tileElement.classList.add('tile')
        rowElement.append(tileElement)
    })
    tileDisplay.append(rowElement)
})

// read keypresses
document['onkeydown'] = function(event) {
    event = event || window.event;
    var key = event.key || event.cursor;
    handleKeypress(key);
};

const handleKeypress = (letter) => {
    if (!isGameOver) {
        if (letter === 'Backspace') {
            deleteLetter()
            return
        }
        if (letter === 'Enter') {
            checkRow()
            return
        }
        if (letter === 'Shift' || letter === 'Control' || letter === 'Tab' || letter === 'OS' || letter === 'Alt' || letter === 'ContextMenu' || letter === 'CapsLock' || letter === 'Escape' || letter === 'Space') {
            return
        }
        addLetter(letter.toUpperCase())
    }
}

const addLetter = (letter) => {
    if (currentTile < 5 && currentRow < 6) {
        const tile = document.getElementById('guessRow-' + currentRow + '-tile-' + currentTile)
        tile.textContent = letter
        guessRows[currentRow][currentTile] = letter
        tile.setAttribute('data', letter)
        currentTile++
    }
}

const deleteLetter = () => {
    if (currentTile > 0) {
        currentTile--
        const tile = document.getElementById('guessRow-' + currentRow + '-tile-' + currentTile)
        tile.textContent = ''
        guessRows[currentRow][currentTile] = ''
        tile.setAttribute('data', '')
    }
}

const checkRow = () => {
    const guess = guessRows[currentRow].join('')
    if (currentTile > 4) {
        flipTile()
        if (wordle == guess) {
            showMessage('You Won!')
            isGameOver = true
            return
        } else {
            if (currentRow >= 5) {
                isGameOver = true
                showMessage('Game Over, You Lose!')
                return
            }
            if (currentRow < 5) {
                currentRow++
                currentTile = 0
            }
        }
    }
}

const showMessage = (message) => {
    const messageElement = document.createElement('p')
    messageElement.textContent = message
    messageDisplay.append(messageElement)
    setTimeout(() => messageDisplay.removeChild(messageElement), 2000)
}

const flipTile = () => {
    const rowTiles = document.querySelector('#guessRow-' + currentRow).childNodes
    let checkWordle = wordle
    const guess = []

    rowTiles.forEach(tile => {
        guess.push({ letter: tile.getAttribute('data'), color: 'grey-overlay' })
    })

    guess.forEach((guess, index) => {
        if (guess.letter == wordle[index]) {
            guess.color = 'green-overlay'
            checkWordle = checkWordle.replace(guess.letter, '')
        }
    })

    guess.forEach(guess => {
        if (checkWordle.includes(guess.letter)) {
            guess.color = 'yellow-overlay'
            checkWordle = checkWordle.replace(guess.letter, '')
        }
    })

    rowTiles.forEach((tile, index) => {
        setTimeout(() => {
            tile.classList.add('flip')
            tile.classList.add(guess[index].color)
        }, 500 * index)
    })
}
