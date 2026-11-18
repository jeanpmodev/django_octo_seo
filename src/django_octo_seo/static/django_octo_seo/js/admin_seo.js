document.addEventListener("DOMContentLoaded", function () {
    function attachCounter(inputId, maxLen, optimalMin) {
        const input = document.getElementById(inputId);
        if (!input) return;

        const container = document.createElement("div");
        container.style.marginTop = "6px";
        container.style.maxWidth = "615px";

        const barTrack = document.createElement("div");
        barTrack.style.height = "6px";
        barTrack.style.width = "100%";
        barTrack.style.backgroundColor = "#e5e7eb";
        barTrack.style.borderRadius = "3px";
        barTrack.style.overflow = "hidden";

        const barFill = document.createElement("div");
        barFill.style.height = "100%";
        barFill.style.width = "0%";
        barFill.style.transition = "width 0.15s ease, background-color 0.15s ease";

        const label = document.createElement("div");
        label.style.fontSize = "11px";
        label.style.marginTop = "4px";
        label.style.fontWeight = "600";

        barTrack.appendChild(barFill);
        container.appendChild(barTrack);
        container.appendChild(label);
        input.parentNode.appendChild(container);

        function update() {
            const len = input.value.length;
            const pct = Math.min((len / maxLen) * 100, 100);
            barFill.style.width = pct + "%";

            let color = "#dc2626";
            let status = "Too short";
            if (len > maxLen) {
                color = "#dc2626";
                status = "Truncated on SERP";
            } else if (len >= optimalMin) {
                color = "#16a34a";
                status = "Optimal length";
            } else if (len > 0) {
                color = "#d97706";
                status = "Below optimal";
            } else {
                status = "Empty";
            }

            barFill.style.backgroundColor = color;
            label.style.color = color;
            label.textContent = len + " / " + maxLen + " characters — " + status;
        }

        input.addEventListener("input", update);
        update();
    }

    function bindLivePreviews() {
        const titleInput = document.getElementById("id_title");
        const descInput = document.getElementById("id_description");
        const urlInput = document.getElementById("id_canonical_url");
        const ogTitleInput = document.getElementById("id_og_title");
        const ogDescInput = document.getElementById("id_og_description");
        const ogImageInput = document.getElementById("id_og_image");

        const serpUrl = document.getElementById("octo-serp-url");
        const serpLink = document.getElementById("octo-serp-link");
        const serpTitle = document.getElementById("octo-serp-title");
        const serpDesc = document.getElementById("octo-serp-desc");
        const ogTitle = document.getElementById("octo-og-title");
        const ogDesc = document.getElementById("octo-og-desc");
        const ogDomain = document.getElementById("octo-og-domain");
        const ogImg = document.getElementById("octo-og-image");

        function sync() {
            const urlVal = (urlInput && urlInput.value.trim()) || "https://ticapsoriginal.com";
            const titleVal = (titleInput && titleInput.value.trim()) || "Django Octo SEO — Enterprise Django SEO Engine";
            const descVal = (descInput && descInput.value.trim()) || "Production-grade, high-performance SEO injection engine for scalable Django infrastructures.";

            if (serpUrl) serpUrl.textContent = urlVal;
            if (serpLink) serpLink.href = urlVal;
            if (serpTitle) serpTitle.textContent = titleVal;
            if (serpDesc) serpDesc.textContent = descVal;

            if (ogTitle) ogTitle.textContent = (ogTitleInput && ogTitleInput.value.trim()) || titleVal;
            if (ogDesc) ogDesc.textContent = (ogDescInput && ogDescInput.value.trim()) || descVal;
            if (ogDomain) {
                try {
                    ogDomain.textContent = new URL(urlVal).hostname.toUpperCase();
                } catch (e) {
                    ogDomain.textContent = "TICAPSORIGINAL.COM";
                }
            }
            if (ogImg && ogImageInput) {
                const imgVal = ogImageInput.value.trim();
                if (imgVal) {
                    ogImg.src = imgVal;
                    ogImg.style.display = "block";
                } else {
                    ogImg.style.display = "none";
                }
            }
        }

        [titleInput, descInput, urlInput, ogTitleInput, ogDescInput, ogImageInput].forEach(function (el) {
            if (el) el.addEventListener("input", sync);
        });
        sync();
    }

    attachCounter("id_title", 60, 30);
    attachCounter("id_description", 160, 100);
    bindLivePreviews();
});
