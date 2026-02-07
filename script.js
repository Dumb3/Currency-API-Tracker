async function getCurrency(currency) {
    try {
        const response = await fetch(`/cotacao/${currency}`);

        if (!response.ok) {
            throw new Error("Erro ao buscar cotação");
        }

        const data = await response.json();

        document.getElementById("response-btn").innerText =
            `${data.currency}: R$ ${data.value}`;

    } catch (error) {
        console.error(error);
        document.getElementById("response-btn").innerText =
            "Erro ao buscar cotação.";
    }
}

document.getElementById("dolar-btn")
    .addEventListener("click", () => getCurrency("USD"));

document.getElementById("euro-btn")
    .addEventListener("click", () => getCurrency("EUR"));
