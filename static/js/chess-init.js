
import { Chess } from './lib/chess.js';

export const chessGame = new Chess();

export let board = null;

export function initBoard() {
  const boardContainer = document.getElementById('board1');
  if (!boardContainer) {
    throw new Error("#board1 element not found in DOM");
  }


    board = Chessboard('board1', {
    position: 'start',
    draggable: false,
    pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png'
    });

    boardContainer.classList.add('visible');
    return board;
}
