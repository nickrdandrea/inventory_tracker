export default function App() {
  const item = {
    id: 1,
    description: 'Pokemon cards',
    category: 'TCG',
    url: 'site.com/pokemoncards',
    vendor_id: 1,
  }

  return (
    <>
      <h1>Tracker</h1>
      <p>
        <b>{item.description}</b>
        <br />
        {item.category}
        <br />
        {item.url}
      </p>
    </>
  );
}