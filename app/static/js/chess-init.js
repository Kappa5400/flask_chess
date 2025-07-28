
import { Chess } from './lib/chess.js';

export const chessGame = new Chess();

export const board = Chessboard('board1', {
  position: 'start',
  draggable: false,
  pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png'
});
