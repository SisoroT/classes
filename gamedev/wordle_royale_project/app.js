const tileDisplay = document.querySelector('.tile-container')
const messageDisplay = document.querySelector('.message-container')

var wordList = [
    // "BANANA",
    // "BETTER",
    // "BEYOND",
    // "BISHOP",
    // "BORDER",
    // "BOTTLE",
    // "BOTTOM",
    // "BOUGHT",
    // "BRANCH",
    // "BREATH",
    // "BRIDGE",
    // "BRIGHT",
    // "BROKEN",
    // "BUDGET",
    // "BURDEN",
    // "BUREAU",
    // "BUTTON",
    // "CAMERA",
    // "CANCER",
    // "CANNOT",
    // "CARBON",
    // "CAREER",
    // "CASTLE",
    // "CASUAL",
    // "CAUGHT",
    // "CENTER",
    // "CENTRE",
    // "CHANCE",
    // "CHANGE",
    // "CHARGE",
    // "CHOICE",
    // "CHOOSE",
    // "CHOSEN",
    // "CHURCH",
    // "CIRCLE",
    // "CLIENT",
    // "CLOSED",
    // "CLOSER",
    // "COFFEE",
    // "COLUMN",
    // "COMBAT",
    // "COMING",
    // "COMMON",
    // "COMPLY",
    // "COPPER",
    // "CORNER",
    // "COSTLY",
    // "COUNTY",
    // "COUPLE",
    // "COURSE",
    // "COVERS",
    // "CREATE",
    // "CREDIT",
    // "CRISIS",
    // "CUSTOM",
    // "DAMAGE",
    // "DANGER",
    // "DEALER",
    // "DEBATE",
    // "DECADE",
    // "DECIDE",
    // "DEFEAT",
    // "DEFEND",
    // "DEFINE",
    // "DEGREE",
    // "DEMAND",
    // "DEPEND",
    // "DEPUTY",
    // "DESERT",
    // "DESIGN",
    // "DESIRE",
    // "DETAIL",
    // "DETECT",
    // "DEVICE",
    // "DIFFER",
    // "DINNER",
    // "DIRECT",
    // "DOCTOR",
    // "DOLLAR",
    // "DOMAIN",
    // "DOUBLE",
    // "DRIVEN",
    // "DRIVER",
    // "DURING",
    // "EASILY",
    // "EATING",
    // "EDITOR",
    // "EFFECT",
    // "EFFORT",
    // "EIGHTH",
    // "EITHER",
    // "ELEVEN",
    // "EMERGE",
    // "EMPIRE",
    // "EMPLOY",
    // "ENABLE",
    // "ENDING",
    // "ENERGY",
    // "ENGAGE",
    // "ENGINE",
    // "ENOUGH",
    // "ENSURE",
    // "ENTIRE",
    // "ENTITY",
    // "EQUITY",
    // "ESCAPE",
    // "ESTATE",
    // "ETHNIC",
    // "EXCEED",
    // "EXCEPT",
    // "EXCESS",
    // "EXPAND",
    // "EXPECT",
    // "EXPERT",
    // "EXPORT",
    // "EXTEND",
    // "EXTENT",
    // "FABRIC",
    // "FACING",
    // "FACTOR",
    // "FAILED",
    // "FAIRLY",
    // "FALLEN",
    // "FAMILY",
    // "FAMOUS",
    // "FATHER",
    // "FELLOW",
    // "FEMALE",
    // "FIGURE",
    // "FILING",
    // "FINGER",
    // "FINISH",
    // "FISCAL",
    // "FLIGHT",
    // "FLYING",
    // "FOLLOW",
    // "FORCED",
    // "FOREST",
    // "FORGET",
    // "FORMAL",
    // "FORMAT",
    // "FORMER",
    // "FOSTER",
    // "FOUGHT",
    // "FOURTH",
    // "FRENCH",
    // "FRIEND",
    // "FUTURE",
    // "GARDEN",
    // "GATHER",
    // "GENDER",
    // "GERMAN",
    // "GLOBAL",
    // "GOLDEN",
    // "GROUND",
    // "GROWTH",
    // "GUILTY",
    // "HANDED",
    // "HANDLE",
    // "HAPPEN",
    // "HARDLY",
    // "HEADED",
    // "HEALTH",
    // "HEIGHT",
    // "HIDDEN",
    // "HOLDER",
    // "HONEST",
    // "IMPACT",
    // "IMPORT",
    // "INCOME",
    // "INDEED",
    // "INJURY",
    // "INSIDE",
    // "INTEND",
    // "INTENT",
    // "INVEST",
    // "ISLAND",
    // "ITSELF",
    // "JERSEY",
    // "JOSEPH",
    // "JUNIOR",
    // "KILLED",
    // "LABOUR",
    // "LATEST",
    // "LATTER",
    // "LAUNCH",
    // "LAWYER",
    // "LEADER",
    // "LEAGUE",
    // "LEAVES",
    // "LEGACY",
    // "LENGTH",
    // "LESSON",
    // "LETTER",
    // "LIGHTS",
    // "LIKELY",
    // "LINKED",
    // "LIQUID",
    // "LISTEN",
    // "LITTLE",
    // "LIVING",
    // "LOSING",
    // "LUCENT",
    // "LUXURY",
    // "MAINLY",
    // "MAKING",
    // "MANAGE",
    // "MANNER",
    // "MANUAL",
    // "MARGIN",
    // "MARINE",
    // "MARKED",
    // "MARKET",
    // "MARTIN",
    // "MASTER",
    // "MATTER",
    // "MATURE",
    // "MEDIUM",
    // "MEMBER",
    // "MEMORY",
    // "MENTAL",
    // "MERELY",
    // "MERGER",
    // "METHOD",
    // "MIDDLE",
    // "MILLER",
    // "MINING",
    // "MINUTE",
    // "MIRROR",
    // "MOBILE",
    // "MODERN",
    // "MODEST",
    // "MODULE",
    // "MOMENT",
    // "MORRIS",
    // "MOSTLY",
    // "MOTHER",
    // "MOTION",
    // "MOVING",
    // "MURDER",
    // "MUSEUM",
    // "MUTUAL",
    // "MYSELF",
    // "NARROW",
    // "NATION",
    // "NATIVE",
    // "NATURE",
    // "NEARBY",
    // "NEARLY",
    // "NIGHTS",
    // "NOBODY",
    // "NORMAL",
    // "NOTICE",
    // "NOTION",
    // "NUMBER",
    // "OBJECT",
    // "OBTAIN",
    // "OFFICE",
    // "OFFSET",
    // "ONLINE",
    // "OPTION",
    // "ORANGE",
    // "ORIGIN",
    // "OUTPUT",
    // "OXFORD",
    // "PACKED",
    // "PALACE",
    // "PARENT",
    // "PARTLY",
    // "PATENT",
    // "PEOPLE",
    // "PERIOD",
    // "PERMIT",
    // "PERSON",
    // "PHRASE",
    // "PICKED",
    // "PLANET",
    // "PLAYER",
    // "PLEASE",
    // "PLENTY",
    // "POCKET",
    // "POLICE",
    // "POLICY",
    // "PREFER",
    // "PRETTY",
    // "PRINCE",
    // "PRISON",
    // "PROFIT",
    // "PROPER",
    // "PROVEN",
    // "PUBLIC",
    // "PURSUE",
    // "RAISED",
    // "RANDOM",
    // "RARELY",
    // "RATHER",
    // "RATING",
    // "READER",
    // "REALLY",
    // "REASON",
    // "RECALL",
    // "RECENT",
    // "RECORD",
    // "REDUCE",
    // "REFORM",
    // "REGARD",
    // "REGIME",
    // "REGION",
    // "RELATE",
    // "RELIEF",
    // "REMAIN",
    // "REMOTE",
    // "REMOVE",
    // "REPAIR",
    // "REPEAT",
    // "REPLAY",
    // "REPORT",
    // "RESCUE",
    // "RESORT",
    // "RESULT",
    // "RETAIL",
    // "RETAIN",
    // "RETURN",
    // "REVEAL",
    // "REVIEW",
    // "REWARD",
    // "RIDING",
    // "RISING",
    // "ROBUST",
    // "RULING",
    // "SAFETY",
    // "SALARY",
    // "SAMPLE",
    // "SAVING",
    // "SAYING",
    // "SCHEME",
    // "SCHOOL",
    // "SCREEN",
    // "SEARCH",
    // "SEASON",
    // "SECOND",
    // "SECRET",
    // "SECTOR",
    // "SECURE",
    // "SEEING",
    // "SELECT",
    // "SELLER",
    // "SENIOR",
    // "SERIES",
    // "SERVER",
    // "SETTLE",
    // "SEVERE",
    // "SEXUAL",
    // "SHOULD",
    // "SIGNAL",
    // "SIGNED",
    // "SILENT",
    // "SILVER",
    // "SIMPLE",
    // "SIMPLY",
    // "SINGLE",
    // "SISTER",
    // "SLIGHT",
    // "SMOOTH",
    // "SOCIAL",
    // "SOLELY",
    // "SOUGHT",
    // "SOURCE",
    // "SOVIET",
    // "SPEECH",
    // "SPIRIT",
    // "SPOKEN",
    // "SPREAD",
    // "SPRING",
    // "SQUARE",
    // "STABLE",
    // "STATUS",
    // "STEADY",
    // "STOLEN",
    // "STRAIN",
    // "STREAM",
    // "STREET",
    // "STRESS",
    // "STRICT",
    // "STRIKE",
    // "STRING",
    // "STRONG",
    // "STRUCK",
    // "STUDIO",
    // "SUBMIT",
    // "SUDDEN",
    // "SUFFER",
    // "SUMMER",
    // "SUMMIT",
    // "SUPPLY",
    // "SURELY",
    // "SURVEY",
    // "SWITCH",
    // "SYMBOL",
    // "SYSTEM",
    // "TAKING",
    // "TALENT",
    // "TARGET",
    // "TAUGHT",
    // "TENANT",
    // "TENDER",
    // "TENNIS",
    // "THANKS",
    // "THEORY",
    // "THIRTY",
    // "THOUGH",
    // "THREAT",
    // "THROWN",
    // "TICKET",
    // "TIMELY",
    // "TIMING",
    // "TISSUE",
    // "TOWARD",
    // "TRAVEL",
    // "TREATY",
    // "TRYING",
    // "TWELVE",
    // "TWENTY",
    // "UNABLE",
    // "UNIQUE",
    // "UNITED",
    // "UNLESS",
    // "UNLIKE",
    // "UPDATE",
    // "USEFUL",
    // "VALLEY",
    // "VARIED",
    // "VENDOR",
    // "VERSUS",
    // "VICTIM",
    // "VISION",
    // "VISUAL",
    // "VOLUME",
    // "WALKER",
    // "WEALTH",
    // "WEEKLY",
    // "WEIGHT",
    // "WHOLLY",
    // "WINDOW",
    // "WINNER",
    // "WINTER",
    // "WITHIN",
    // "WONDER",
    // "WORKER",
    // "WRIGHT",
    // "WRITER",
    // "YELLOW",
    "SUPERB"
];

const wordle = wordList[Math.floor(Math.random() * wordList.length)];

let guessRows = [
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
]
let currentRow = 0
let currentTile = 0
let totalRows = 6
let isGameOver = false
let firstYellow = true
let firstGreen = true

// load initial rows
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

// function to add a row
// const addRow = () => {
//     guessRows.push(['', '', '', '', '', ''])
//     for (let i = totalRows; i < guessRows.length; i++) {
//         const rowElement = document.createElement('div')
//         rowElement.setAttribute('id', 'guessRow-' + i)
//         guessRows[1].forEach((_guess, guessIndex) => {
//             const tileElement = document.createElement('div')
//             tileElement.setAttribute('id', 'guessRow-' + i + '-tile-' + guessIndex)
//             tileElement.classList.add('tile')
//             rowElement.append(tileElement)
//         })
//         tileDisplay.append(rowElement)
//     }
//     totalRows++
// }

// function to add a row
const addRow = () => {
    guessRows.push(['', '', '', '', '', ''])

    const rowElement = document.createElement('div')
    rowElement.setAttribute('id', 'guessRow-' + totalRows)
    guessRows[0].forEach((_guess, guessIndex) => {
        const tileElement = document.createElement('div')
        tileElement.setAttribute('id', 'guessRow-' + (totalRows) + '-tile-' + guessIndex)
        tileElement.classList.add('tile')
        rowElement.append(tileElement)
    })
    tileDisplay.append(rowElement)

    totalRows++
}


// function to delete a row
const deleteRow = () => {
    guessRows.pop()
    document.getElementById('guessRow-' + (totalRows - 1)).remove()
    totalRows--
}


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
    if (currentTile < 6 && currentRow < totalRows) {
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
    if (currentTile > 5) {
        flipTile()
        if (wordle == guess) {
            showMessage('You Won!')
            isGameOver = true
            return
        } else {
            if (currentRow >= totalRows - 1) {
                isGameOver = true
                showMessage('Game Over, You Lose!')
                return
            }
            if (currentRow < totalRows - 1) {
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
    let infoMade = false

    rowTiles.forEach(tile => {
        guess.push({ letter: tile.getAttribute('data'), color: 'grey-overlay' })
    })

    guess.forEach((guess, index) => {
        if (guess.letter == wordle[index]) {
            infoMade = true
            // add 2 new rows the first time there is a green tile
            if (firstGreen) {
                addRow()
                addRow()
                firstGreen = false
            }
            guess.color = 'green-overlay'
            checkWordle = checkWordle.replace(guess.letter, '')
        }
    })

    guess.forEach(guess => {
        if (checkWordle.includes(guess.letter)) {
            infoMade = true
            // add 1 new row the first time there is a yellow tile
            if (firstYellow) {
                addRow()
                firstYellow = false
            }
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

    // if no information is made then delete a row
    if (!infoMade) {
        deleteRow()
    }
}
