import { Chess } from './lib/chess.js';

document.addEventListener('DOMContentLoaded', () => {
  const content = document.getElementById('main-content');

  // Initialize the chess game first
  const game = new Chess();

  // Then the board
  const board = Chessboard('board1', {
    position: 'start',
    draggable: false,
    pieceTheme: '/static/img/chesspieces/wikipedia/{piece}.png'
  });

  // Defer visibility until layout stabilizes
  requestAnimationFrame(() => {
    // small delay ensures layout paint happens before showing
    setTimeout(() => {
      content.classList.add('loaded');
    }, 50); // Adjust this if needed
  });
});
