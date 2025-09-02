const form = document.getElementById("upload-form");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const file1 = document.getElementById("file1").files[0];

  const file2 = document.getElementById("file2").files[0];

  if (!file1 || !file2) {
    alert("Please make sure that there are two files");
    return;
  }

  const formData = new FormData();
  formData.append("followers", file1);
  formData.append("followings", file2);

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    document.getElementById("unfollowers-output").innerHTML = `
      <h3>Unfollowers</h3>
      <pre>${data.unfollowers.preview}</pre>
    `;
  } catch (err) {
    console.error("Upload failed:", err);
    alert("Upload failed: " + err);
  }
});
