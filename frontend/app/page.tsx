import { useEffect, useState } from "react";

export default function Home() {
  const [articles, setArticles] = useState([]);
  const [form, setForm] = useState({
    id: "",
    name: "",
    price: "",
    in_stock: true
  });

  // 🟢 fetch articles
  useEffect(() => {
    fetchArticles();
  }, []);

  const fetchArticles = () => {
    fetch("http://127.0.0.1:8000/articles")
      .then(res => res.json())
      .then(data => setArticles(data));
  };

  // 🟢 ajouter article
  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch("http://127.0.0.1:8000/articles", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: parseInt(form.id),
        name: form.name,
        price: parseFloat(form.price),
        in_stock: form.in_stock
      })
    });
    setForm({ id: "", name: "", price: "", in_stock: true });
    fetchArticles();
  };

  // 🟢 delete article
  const handleDelete = async (id) => {
    await fetch(`http://127.0.0.1:8000/articles/${id}`, { method: "DELETE" });
    fetchArticles();
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Liste des articles</h1>

      {/* form ajouter article */}
      <form onSubmit={handleSubmit} style={{ marginBottom: "20px" }}>
        <input
          type="number"
          placeholder="ID"
          value={form.id}
          onChange={(e) => setForm({ ...form, id: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Nom"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
          required
        />
        <input
          type="number"
          placeholder="Prix"
          value={form.price}
          onChange={(e) => setForm({ ...form, price: e.target.value })}
          required
        />
        <select
          value={form.in_stock}
          onChange={(e) => setForm({ ...form, in_stock: e.target.value === "true" })}
        >
          <option value={true}>En stock</option>
          <option value={false}>Rupture</option>
        </select>
        <button type="submit">Ajouter</button>
      </form>

      {/* liste articles */}
      <ul>
        {articles.map(a => (
          <li key={a.id} style={{ marginBottom: "10px" }}>
            {a.name} - {a.price} DT - {a.in_stock ? "En stock" : "Rupture"}
            <button onClick={() => handleDelete(a.id)} style={{ marginLeft: "10px" }}>
              Supprimer
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}