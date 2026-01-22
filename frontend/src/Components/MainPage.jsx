import React, { useState } from "react";
import { generateProductDescription } from "../services/api";

const MainPage = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState("");

  const [formData, setFormData] = useState({
    product_name: "",
    material: "",
    color: "",
    audience: "",
    max_words: 10,
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult("");

    try {
      const res = await generateProductDescription(formData);
      console.log(res.data);

      // Access description inside data
      const descriptions = res.data.data.description;

      // Combine 3 descriptions to show on page
      setResult(`
1️⃣ ${descriptions.description_1}

2️⃣ ${descriptions.description_2 || "N/A"}

3️⃣ ${descriptions.description_3 || "N/A"}
`);
    } catch (error) {
      console.log(error);
      setResult("❌ Error generating description");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 px-4">
      <div className="w-full max-w-lg bg-white rounded-xl shadow-lg p-6">
        <h1 className="text-2xl font-bold text-center mb-6 text-indigo-600">
          AI Product Description Generator
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            name="product_name"
            placeholder="Product Name"
            value={formData.product_name}
            onChange={handleChange}
            required
            className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />

          <input
            type="text"
            name="material"
            placeholder="Material"
            value={formData.material}
            onChange={handleChange}
            required
            className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />

          <input
            type="text"
            name="color"
            placeholder="Color"
            value={formData.color}
            onChange={handleChange}
            required
            className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />

          <input
            type="text"
            name="audience"
            placeholder="Audience (Men / Women / Kids)"
            value={formData.audience}
            onChange={handleChange}
            required
            className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />

          <input
            type="number"
            name="max_words"
            placeholder="Max Words"
            value={formData.max_words}
            onChange={handleChange}
            min={5}
            max={200}
            className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400"
          />

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-indigo-600 text-white py-3 rounded-md font-semibold hover:bg-indigo-700 transition disabled:opacity-60"
          >
            {loading ? "Generating..." : "Generate Description"}
          </button>
        </form>

        <div className="space-y-2 text-gray-700">
          {result.split("\n").map((line, i) => (
            <p key={i}>{line}</p>
          ))}
        </div>
      </div>
    </div>
  );
};

export default MainPage;
