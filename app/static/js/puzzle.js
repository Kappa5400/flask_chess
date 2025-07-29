import { chessGame, board } from './chess-init.js';

const data = document.getElementById('puzzle-data');
const puzzleId = data.dataset.id;
const puzzlePgn = data.dataset.pgn;

chessGame.loadPgn(puzzlePgn);

console.log(chessGame.pgn());

board.position(chessGame.fen());

