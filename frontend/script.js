const API_URL = "";

const urlInput = document.getElementById("url");
const button = document.getElementById("auditBtn");

const loading = document.getElementById("loading");
const error = document.getElementById("error");
const report = document.getElementById("report");

async function auditURL() {

    let url = urlInput.value.trim();

    error.classList.add("hidden");
    report.classList.add("hidden");

    if (url === "") {

        error.innerText = "Please enter a website URL.";

        error.classList.remove("hidden");

        return;
    }

    if (
        !url.startsWith("http://") &&
        !url.startsWith("https://")
    ) {
        url = "https://" + url;
    }

    loading.classList.remove("hidden");

    button.disabled = true;

    button.innerText = "Analyzing...";

    try {

        const response = await fetch("/audit", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                url: url

            })

        });

        const data = await response.json();

        loading.classList.add("hidden");

        button.disabled = false;

        button.innerText = "Generate Report";

        if (!response.ok) {

            error.innerText =
                data.error?.message ||
                "Audit failed.";

            error.classList.remove("hidden");

            return;
        }

        report.classList.remove("hidden");

        populateReport(data);

    }

    catch (err) {

        loading.classList.add("hidden");

        button.disabled = false;

        button.innerText = "Generate Report";

        error.innerText =
            "Unable to connect to backend.";

        error.classList.remove("hidden");

    }

}

function populateReport(data) {

    // Executive Summary

    const badge = document.getElementById("statusBadge");

    if (data.status_code >= 200 && data.status_code < 300) {

        badge.innerText = "ONLINE";

        badge.className = "badge good";

    }
    else {

        badge.innerText = "ERROR";

        badge.className = "badge bad";

    }

    document.getElementById("responseTime").innerText =
        `${Number(data.response_time_ms).toFixed(2)} ms`;

        document.getElementById("apiResponseTime").innerText =
    `${Number(data.api_response_time_ms).toFixed(2)} ms`;

   document.getElementById("cached").innerText =
    data.cache.hit
        ? "HIT ✅"
        : "MISS ❌";

    document.getElementById("cacheStatus").innerText =
    data.cache.hit
        ? "Served from Redis Cache"
        : "Fetched from Origin Server";

document.getElementById("cacheTTL").innerText =
    `${data.cache.ttl_remaining} sec`;

    document.getElementById("https").innerText =
        data.https
            ? "Enabled 🔒"
            : "Disabled 🔓";


    // URL Information

    document.getElementById("requestedUrl").innerText =
        data.url;

    document.getElementById("finalUrl").innerText =
        data.final_url;

    document.getElementById("title").innerText =
        data.title || "-";

    document.getElementById("requestId").innerText =
        data.request_id;


    // Performance

    document.getElementById("statusCode").innerText =
        data.status_code;

    document.getElementById("responseTime2").innerText =
        `${Number(data.response_time_ms).toFixed(2)} ms`;

    document.getElementById("server").innerText =
        data.server || "-";

    document.getElementById("redirects").innerText =
        data.redirects;

    document.getElementById("contentLength").innerText =
        `${(data.content_length / 1024).toFixed(1)} KB`;

    document.getElementById("contentType").innerText =
        data.content_type;


    // Security

    setSecurity(
        "sts",
        data.security_headers.strict_transport_security,
        "Present",
        "Missing"
    );

    setSecurity(
        "csp",
        data.security_headers.content_security_policy,
        "Present",
        "Missing"
    );

    setSecurity(
        "xframe",
        data.security_headers.x_frame_options,
        "Present",
        "Missing"
    );

    setSecurity(
        "xcontent",
        data.security_headers.x_content_type_options,
        "Present",
        "Missing"
    );

}

function setSecurity(id, enabled) {

    const element = document.getElementById(id);

    if (enabled) {

        element.innerHTML = "✅ Present (Good)";
        element.className = "good";

    }
    else {

        element.innerHTML = "❌ Missing (Potential Risk)";
        element.className = "bad";

    }

}


urlInput.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

        auditURL();

    }

});


window.onload = () => {

    urlInput.focus();

};