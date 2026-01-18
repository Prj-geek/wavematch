export default function SongCard({ song }) {
  return (
    <div className="song-card">
      <strong>{song.track_name}</strong>
      <p>{song.artist_name}</p>
      {song.similarity !== undefined && (
        <small>Similarity: {song.similarity.toFixed(2)}</small>
      )}
    </div>
  );
}
