import { chessGame, board } from './chess-init.js';

while (!chessGame.isGameOver()) {
  const moves = chessGame.moves();
  const move = moves[Math.floor(Math.random() * moves.length)];
  chessGame.move(move);
}

console.log(chessGame.pgn());

board.position(chessGame.fen());
