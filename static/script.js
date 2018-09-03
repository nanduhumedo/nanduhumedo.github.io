var request = new XMLHttpRequest();

var guess = document.getElementById("frm1");

var xhttp = new XMLHttpRequest();
var guessIndex = -1;
var puzzle = [];
var current_puzzle = [];
var score = 0;
var show_correct = false;
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
  puzzle = this.responseText.split("\n");
  current_puzzle = []
  current_puzzle[0] = puzzle[0][0]
  for (i = 1; i < puzzle.length - 2; i++) {
      current_puzzle[i] = "\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0";
  }
  current_puzzle[puzzle.length - 2] = puzzle[puzzle.length - 2][0]

  var current_puzzle_string = ""
  for (i = 0; i < current_puzzle.length; i++) {
      current_puzzle_string += "<div id=puzzle_word_" + i + ">";
      for (var j = 0; j < puzzle[i].length; j++) {
        current_puzzle_string += "<div style=float:left; id=puzzle_word_" + i + "_letter_" + j + ">";
        if (j < current_puzzle[i].trim().length) {
            current_puzzle_string += puzzle[i][j];
        }
        else {
            current_puzzle_string += "|";
        }
        current_puzzle_string += "</div>"
      }
      current_puzzle_string +=       "</div>" + "<br/>"
  }

  document.getElementById("demo").innerHTML =
  current_puzzle_string;
  var words = []
  for (i = 0; i < current_puzzle.length; i++) {
     words[i] = document.getElementById("puzzle_word_" + i);
     words[i].addEventListener("click", bind_click(i));

  }

  function bind_click(i) {
    return function() {
        if (i == 0 || i == puzzle.length - 2 ) {
            update_current_puzzle_string(i, current_puzzle[i].trim().length)
        }
        else if (current_puzzle[i-1].trim().length != 0 || current_puzzle[i+1].trim().length != 0) {
            update_current_puzzle_string(i, current_puzzle[i].trim().length)
        }
    }

  }

  function update_current_puzzle_string(i, j) {
    document.getElementById("puzzle_word_" + i + "_letter_" + j).innerHTML = puzzle[i][j];
    current_puzzle[i] = current_puzzle[i].trim()
    current_puzzle[i] += puzzle[i][j];
    guessIndex = i;

  }



}
};
xhttp.open("GET", "/get_chain", true);
xhttp.send();

function checkGuess() {
    var currentGuess = guess.elements[0].value;
    if (currentGuess.trim() == puzzle[guessIndex].trim()) {
        alert("Correct!");
        document.getElementById("guessStatus").innerHTML = "Correct!";
        finish_current_puzzle_string(guessIndex);
        score += 1;
        document.getElementById("score").innerHTML = "Score: " + score;
    }
    else {
        alert("WROOOOOOOOONG! (Maybe check if caps lock was on?)")
        document.getElementById("guessStatus").innerHTML = "WROOOOOOOOONG! (Maybe check if caps lock was on?)";

    }

}

function finish_current_puzzle_string(i) {
     for (var j= 0; j < puzzle[i].length; j++) {
        document.getElementById("puzzle_word_" + i + "_letter_" + j).innerHTML = puzzle[i][j];
     }
    current_puzzle[i] = puzzle[i];
    guessIndex = i;

}

function toggle_show_correct() {
     if (show_correct) {
        document.getElementById("correct").innerHTML = puzzle.join("<br/>");
     }
     else {
        document.getElementById("correct").innerHTML = "";
     }
     show_correct = !show_correct;
}
