import SongCard from "./SongCard";

export default function RecommendationList({ recommendations }) {
  if (!recommendations || !recommendations.length) {
    return <p>No recommendations yet</p>;
  }

  return (
    <div>
      <h3>Recommendations</h3>
      {recommendations.map((song, index) => (
        <SongCard key={index} song={song} />
      ))}
    </div>
  );
}
