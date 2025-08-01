import { chessGame, initBoard } from './chess-init.js';

document.addEventListener('DOMContentLoaded', () => {
  const board = initBoard();

  const boardContainer = document.getElementById('board1');
  const data = document.getElementById('puzzle-data');
  const puzzlePgn = data.dataset.pgn;

  chessGame.loadPgn(puzzlePgn);
  console.log(chessGame.pgn());

  board.position(chessGame.fen());
});
