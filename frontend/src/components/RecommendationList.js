import SongCard from "./SongCard";

export default function RecommendationList({ recommendations }) {
  if (!recommendations || !recommendations.length) {
    return <p className="muted">No recommendations yet</p>;
  }

  return (
    <div className="recommendations">
      {recommendations.map((song, index) => (
        <SongCard key={index} song={song} />
      ))}
    </div>
  );
}
