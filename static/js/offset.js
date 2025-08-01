export async function injectPuzzleLink(offset) {
  try {
    const res = await fetch(`/api/puzzle/${offset}`);
    if (!res.ok) throw new Error("Puzzle not found");
    const puzzle = await res.json();

    const link = document.getElementById(`puzzle-link-${offset + 1}`);
    const numberSpan = document.getElementById(`puzzle-number-${offset + 1}`);

    if (link && numberSpan) {
      link.href = `/puzzle/${puzzle.id}`;
      link.textContent = "Click me!";
      numberSpan.textContent = offset + 1;
    }
  } catch {
    const link = document.getElementById(`puzzle-link-${offset + 1}`);
    if (link) link.textContent = "Puzzle not available";
  }
}
