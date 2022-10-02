export default function ItemFeed() {
  const items = [
    {
      id: 1,
      description: 'Pokemon cards',
      category: 'TCG',
      url: 'site.com/pokemoncards',
      vendor_id: 1,
    },
    {
      id: 2,
      description: 'YuGIOh cards',
      category: 'TCG',
      url: 'site.com/yugioh',
      vendor_id: 1,
    },
  ];

  return (
    <>
      {items.length === 0 ? (
        <p>There are no items to display.</p>
      ) : (
        items.map((item) => {
          return (
            <p key={item.id}>
              <b>{item.description}</b>
              <br />
              {item.category}
              <br />
              {item.url}
            </p>
          );
        })
      )}
    </>
  );
}
