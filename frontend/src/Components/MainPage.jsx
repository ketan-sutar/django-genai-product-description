import React, { useState } from "react";

const MainPage = () => {
  const [loading, setLoading] = useState(false)
  return (
    <div>
      <h1>AI Product Description Generator</h1>
      <form action="">
        <input type="text" name="product_name" placeholder="Product Name" />
        <input type="text" name="material" placeholder="Material" />
        <input type="text" name="color" placeholder="Color" />
        <input type="text" name="audience" placeholder="Audience" />
        <input type="number" name="max_words" placeholder="Max Words" />


        <button>{loading ? "Loading...":"Generate Description"}</button>
      </form>
    </div>
  );
};

export default MainPage;
