import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os

st.set_page_config(
    page_title="Wuzzuf Job Market Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    base   = os.path.dirname(os.path.abspath(__file__))
    df     = pd.read_csv(os.path.join(base, "data_jobs_clean.csv"))
    skills = pd.read_csv(os.path.join(base, "skills_analysis.csv"))
    return df, skills

df, skills_df = load_data()

TOTAL_JOBS = 2533
BLUE       = "#1a4ed8"
BLUE_LIGHT = "#3b82f6"
BLUE_PALE  = "#bfdbfe"
BLUE_DARK  = "#0f2a6e"
GREY       = "#94a3b8"
PCFG       = {"displayModeBar": False, "responsive": True}

# ─────────────────────────────────────────────
#  CSS  — fully responsive
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=Space+Grotesk:wght@500;600;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.stApp {
    background: linear-gradient(145deg, #0a1e52 0%, #1442c8 45%, #1d55e0 75%, #2260f0 100%);
    min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: clamp(12px, 3vw, 28px) clamp(12px, 3vw, 32px) !important;
    max-width: 100% !important;
}
div[data-testid="stAppViewBlockContainer"] { padding: 0 !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* ── Shell ── */
.dashboard-block {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 32px 80px rgba(0,0,0,0.35), 0 8px 24px rgba(0,0,0,0.20),
                inset 0 1px 0 rgba(255,255,255,0.12);
}

/* ── Topbar ── */
.topbar {
    padding: 12px clamp(14px,3vw,28px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
    border-bottom: 1px solid rgba(255,255,255,0.10);
    background: rgba(255,255,255,0.04);
}
.logo-badge {
    background: white;
    border-radius: 9px;
    padding: 5px 14px;
    display: inline-flex;
    align-items: center;
    font-family: 'Space Grotesk', sans-serif;
    box-shadow: 0 2px 12px rgba(0,0,0,0.15);
    flex-shrink: 0;
}
.lw { color: #1a4ed8; font-weight: 700; font-size: clamp(13px,2vw,16px); }
.lr { color: #1a4ed8; font-size: clamp(13px,2vw,16px); letter-spacing: 3px; font-weight: 400; }
.sep { width:1px; height:28px; background:rgba(255,255,255,0.18); margin:0 14px; flex-shrink:0; }
.t-title { font-size:clamp(12px,2vw,14px); font-weight:500; color:white; }
.t-sub   { font-size:clamp(10px,1.5vw,12px); color:rgba(255,255,255,0.50); margin-top:1px; }
.topbar-pills { display:flex; gap:8px; flex-wrap:wrap; }
.pill-o { border:1px solid rgba(255,255,255,0.28); color:rgba(255,255,255,0.85);
          font-size:clamp(10px,1.5vw,12px); padding:4px 12px; border-radius:20px; white-space:nowrap; }
.pill-f { background:white; color:#1a4ed8; font-size:clamp(10px,1.5vw,12px); font-weight:600;
          padding:4px 12px; border-radius:20px; white-space:nowrap;
          box-shadow:0 2px 8px rgba(0,0,0,0.12); }

/* ── KPI cards ── */
.kcard {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 14px;
    padding: clamp(12px,2vw,18px) clamp(14px,2.5vw,22px) clamp(10px,1.5vw,14px);
    height: 100%;
    transition: background 0.2s, transform 0.15s;
    margin-bottom: 2px;
}
.kcard:hover { background:rgba(255,255,255,0.14); transform:translateY(-2px); }
.klbl {
    font-size: clamp(9px,1.2vw,11px);
    color: rgba(255,255,255,0.55);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.7px;
    margin-bottom: 7px;
}
.kval {
    font-size: clamp(22px,4vw,34px);
    font-weight: 600;
    color: white;
    line-height: 1;
    font-family: 'Space Grotesk', sans-serif;
    letter-spacing: -1px;
}
.kval-unit { font-size:clamp(12px,1.8vw,16px); opacity:0.60; margin-left:2px; letter-spacing:0; }
.ksub { font-size:clamp(10px,1.4vw,12px); color:rgba(255,255,255,0.45); margin-top:6px; }

/* ── White cards ── */
.wcard {
    background: white;
    border-radius: 14px;
    padding: clamp(12px,2vw,18px);
    height: 100%;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
}
.ctit {
    font-size: clamp(11px,1.6vw,13px);
    font-weight: 600;
    color: #0f2a6e;
    margin-bottom: 10px;
    font-family: 'Space Grotesk', sans-serif;
}

/* ── Insight ── */
.ins {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.14);
    border-left: 4px solid rgba(255,255,255,0.7);
    border-radius: 12px;
    padding: clamp(10px,2vw,14px) clamp(14px,2.5vw,22px);
    margin-top: 6px;
}
.it { font-size:clamp(11px,1.6vw,13px); color:rgba(255,255,255,0.90); line-height:1.8; }
.it strong {
    font-weight: 600;
    background: rgba(255,255,255,0.14);
    padding: 1px 8px;
    border-radius: 5px;
    color: white;
}

/* ── Company rows ── */
.corow {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: clamp(6px,1vw,8px) clamp(8px,1.5vw,13px);
    background: #f0f6ff;
    border-radius: 9px;
    margin-bottom: 6px;
    transition: background 0.15s;
}
.corow:hover { background:#dbeafe; }
.corow:last-child { margin-bottom:0; }
.con { font-size:clamp(11px,1.5vw,13px); color:#0f2a6e; font-weight:500; }
.cob { font-size:clamp(10px,1.3vw,12px); font-weight:600; color:#1a4ed8;
       background:#dbeafe; padding:2px 10px; border-radius:20px; white-space:nowrap; }

/* ── Tabs ── */
div[data-baseweb="tab-list"] {
    background: rgba(0,0,0,0.08) !important;
    border-bottom: 1px solid rgba(255,255,255,0.08) !important;
    padding: 0 clamp(12px,3vw,28px) !important;
    gap: 0 !important;
    overflow-x: auto !important;
}
div[data-baseweb="tab"] {
    background: transparent !important;
    color: rgba(255,255,255,0.45) !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    font-size: clamp(11px,1.8vw,13.5px) !important;
    padding: 11px clamp(10px,2vw,24px) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 400 !important;
    margin-bottom: -1px !important;
    white-space: nowrap !important;
}
div[data-baseweb="tab"]:hover { color:rgba(255,255,255,0.80) !important; }
div[aria-selected="true"][data-baseweb="tab"] {
    color: white !important;
    border-bottom: 2px solid white !important;
    font-weight: 500 !important;
}
div[data-baseweb="tab-highlight"], div[data-baseweb="tab-border"] { display:none !important; }

/* ── Filter selects ── */
div[data-testid="stSelectbox"] label { display:none !important; }
div[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.18) !important;
    border-radius: 9px !important;
    color: white !important;
    font-size: clamp(10px,1.4vw,12.5px) !important;
    min-height: 34px !important;
}
div[data-testid="stSelectbox"] > div > div:hover { background:rgba(255,255,255,0.14) !important; }
div[data-testid="stSelectbox"] svg { fill:rgba(255,255,255,0.6) !important; }

/* ── Content padding ── */
.content-area { padding: clamp(14px,3vw,24px) clamp(14px,3vw,28px); }
.gap-sm { height:10px; }
.gap-md { height:clamp(12px,2vw,18px); }

/* ── MOBILE: stack all columns ── */
@media screen and (max-width: 640px) {
    div[data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 100% !important;
    }
    .kval { font-size: 26px !important; }
    .sep  { display: none; }
    .topbar { gap: 8px; }
    .wcard, .kcard { margin-bottom: 10px; }
}

/* ── TABLET: 2-column grid for charts ── */
@media screen and (min-width: 641px) and (max-width: 960px) {
    div[data-testid="column"] {
        width: 50% !important;
        flex: 1 1 50% !important;
        min-width: 50% !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  CHART HELPERS
# ─────────────────────────────────────────────
def bar_h(y_vals, x_vals, height=260):
    mx = max(x_vals) if x_vals else 1
    colors = [f"rgba(26,78,216,{0.40 + 0.60*(v/mx):.2f})" for v in x_vals]
    fig = go.Figure(go.Bar(
        x=x_vals, y=y_vals, orientation='h',
        marker=dict(color=colors, line=dict(width=0), cornerradius=5),
        text=x_vals, textposition='outside',
        textfont=dict(size=12, color="#1e40af", family="DM Sans"),
        hovertemplate="<b>%{y}</b><br>%{x} jobs<extra></extra>",
        cliponaxis=False,
    ))
    fig.update_layout(
        margin=dict(l=4, r=52, t=4, b=4), height=height,
        paper_bgcolor='white', plot_bgcolor='white',
        xaxis=dict(showgrid=False, visible=False, range=[0, mx*1.42]),
        yaxis=dict(showgrid=False, tickfont=dict(size=12, color="#1e40af", family="DM Sans"), automargin=True),
        showlegend=False,
        hoverlabel=dict(bgcolor="#0f2a6e", font_size=12, font_family="DM Sans"),
    )
    return fig

def bar_v(x_vals, y_vals, colors=None, height=210):
    mx = max(y_vals) if y_vals else 1
    if colors is None:
        colors = [f"rgba(26,78,216,{0.40 + 0.60*(v/mx):.2f})" for v in y_vals]
    fig = go.Figure(go.Bar(
        x=x_vals, y=y_vals,
        marker=dict(color=colors, line=dict(width=0), cornerradius=5),
        text=y_vals, textposition='outside',
        textfont=dict(size=12, color="#1e40af", family="DM Sans"),
        hovertemplate="<b>%{x}</b><br>%{y} jobs<extra></extra>",
        cliponaxis=False,
    ))
    fig.update_layout(
        margin=dict(l=4, r=4, t=14, b=4), height=height,
        paper_bgcolor='white', plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickfont=dict(size=11, color="#1e40af", family="DM Sans"), automargin=True),
        yaxis=dict(showgrid=False, visible=False, range=[0, mx*1.30]),
        showlegend=False,
        hoverlabel=dict(bgcolor="#0f2a6e", font_size=12, font_family="DM Sans"),
    )
    return fig

def grouped_bar(categories, data_vals, all_vals, height=240):
    mx = max(max(data_vals), max(all_vals))
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Data Jobs", x=categories, y=data_vals,
        marker=dict(color=BLUE, line=dict(width=0), cornerradius=5),
        text=[f"{v}%" for v in data_vals], textposition='outside',
        textfont=dict(size=12, color="#1e40af", family="DM Sans"),
        hovertemplate="<b>%{x}</b><br>Data Jobs: %{y}%<extra></extra>",
        cliponaxis=False,
    ))
    fig.add_trace(go.Bar(
        name="All Jobs", x=categories, y=all_vals,
        marker=dict(color=GREY, line=dict(width=0), cornerradius=5),
        text=[f"{v}%" for v in all_vals], textposition='outside',
        textfont=dict(size=12, color="#475569", family="DM Sans"),
        hovertemplate="<b>%{x}</b><br>All Jobs: %{y}%<extra></extra>",
        cliponaxis=False,
    ))
    fig.update_layout(
        barmode='group',
        margin=dict(l=4, r=4, t=36, b=4), height=height,
        paper_bgcolor='white', plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickfont=dict(size=12, color="#1e40af", family="DM Sans")),
        yaxis=dict(showgrid=False, visible=False, range=[0, mx*1.35]),
        legend=dict(orientation='h', yanchor='bottom', y=1.01, xanchor='left', x=0,
                    font=dict(size=12, color="#1e40af", family="DM Sans"), bgcolor='rgba(0,0,0,0)'),
        bargap=0.22, bargroupgap=0.06,
        hoverlabel=dict(bgcolor="#0f2a6e", font_size=12, font_family="DM Sans"),
    )
    return fig


# ─────────────────────────────────────────────
#  LAYOUT
# ─────────────────────────────────────────────
st.markdown('<div class="dashboard-block">', unsafe_allow_html=True)

# Topbar
st.markdown("""
<div class="topbar">
  <div style="display:flex;align-items:center;flex-wrap:wrap;gap:10px;">
    <div class="logo-badge"><span class="lw">W</span><span class="lr">UZZUF</span></div>
    <div class="sep"></div>
    <div>
      <div class="t-title">Job Market Analysis</div>
      <div class="t-sub">Egypt · 2026 · Marwan Hassan Essa</div>
    </div>
  </div>
  <div class="topbar-pills">
    <div class="pill-o">2,533 listings</div>
    <div class="pill-f">209 data jobs</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Filter bar
st.markdown('<div style="padding:10px clamp(14px,3vw,28px) 9px;border-bottom:1px solid rgba(255,255,255,0.08);background:rgba(0,0,0,0.08);">', unsafe_allow_html=True)
fc = st.columns([0.07, 0.16, 0.16, 0.16, 0.16, 0.29])
with fc[0]:
    st.markdown('<p style="color:rgba(255,255,255,0.45);font-size:12px;margin-top:8px;white-space:nowrap;">Filter:</p>', unsafe_allow_html=True)
with fc[1]:
    city_filter  = st.selectbox("c", ["All cities","Cairo","Giza","Alexandria"], label_visibility="collapsed", key="city")
with fc[2]:
    model_filter = st.selectbox("m", ["Work model","On-site","Hybrid","Remote"], label_visibility="collapsed", key="model")
with fc[3]:
    exp_filter   = st.selectbox("e", ["Experience","Entry level","Experienced","Manager"], label_visibility="collapsed", key="exp")
with fc[4]:
    type_filter  = st.selectbox("t", ["Job type","Full time","Part time"], label_visibility="collapsed", key="jtype")
st.markdown('</div>', unsafe_allow_html=True)

# Filter logic
filtered = df.copy()
if city_filter  != "All cities": filtered = filtered[filtered["Government"] == city_filter]
if model_filter != "Work model":  filtered = filtered[filtered["On-site/Remote"] == model_filter]
if exp_filter   != "Experience":
    lvl = {"Entry level":"Entry Level","Experienced":"Experienced","Manager":"Manager"}[exp_filter]
    filtered = filtered[filtered["Experience Level"] == lvl]
if type_filter  != "Job type":
    t = {"Full time":"Full Time","Part time":"Part Time"}[type_filter]
    filtered = filtered[filtered["Job Type"].str.contains(t, na=False)]
n = len(filtered)

tab1, tab2 = st.tabs(["  📊  Data jobs overview  ", "  ⚖️  Data vs general market  "])

# ══════════════════════════════════════════════
#  TAB 1
# ══════════════════════════════════════════════
with tab1:
    st.markdown('<div class="content-area">', unsafe_allow_html=True)

    # KPIs
    k1, k2, k3, k4 = st.columns(4, gap="small")
    with k1:
        st.markdown(f"""<div class="kcard">
            <div class="klbl">Total Data Jobs</div>
            <div class="kval">{n}<span class="kval-unit"> jobs</span></div>
            <div class="ksub">of {TOTAL_JOBS:,} total listings</div>
        </div>""", unsafe_allow_html=True)
    with k2:
        if "Min Exp" in filtered.columns and filtered["Min Exp"].notna().any():
            avg_min = round(filtered["Min Exp"].mean(), 1)
            avg_max = round(filtered["Max Exp"].mean(), 1)
        else:
            avg_min, avg_max = 2.5, 4.6
        st.markdown(f"""<div class="kcard">
            <div class="klbl">Experience Range</div>
            <div class="kval">{avg_min:.0f}–{avg_max:.0f}<span class="kval-unit"> yrs</span></div>
            <div class="ksub">average min–max required</div>
        </div>""", unsafe_allow_html=True)
    with k3:
        remote_n   = (filtered["On-site/Remote"] == "Remote").sum()
        remote_pct = remote_n / max(n, 1) * 100
        st.markdown(f"""<div class="kcard">
            <div class="klbl">Remote Jobs</div>
            <div class="kval">{remote_pct:.1f}<span class="kval-unit">%</span></div>
            <div class="ksub">{remote_n} jobs · vs 3.9% all jobs</div>
        </div>""", unsafe_allow_html=True)
    with k4:
        cairo_n   = (filtered["Government"] == "Cairo").sum()
        cairo_pct = cairo_n / max(n, 1) * 100
        st.markdown(f"""<div class="kcard">
            <div class="klbl">Cairo Concentration</div>
            <div class="kval">{cairo_pct:.1f}<span class="kval-unit">%</span></div>
            <div class="ksub">{cairo_n} jobs · vs 66.1% all jobs</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="gap-md"></div>', unsafe_allow_html=True)

    # Row 1
    c1, c2, c3 = st.columns(3, gap="small")
    with c1:
        st.markdown('<div class="wcard"><div class="ctit">🛠️ Top Skills in Data Jobs</div>', unsafe_allow_html=True)
        top_s = skills_df[skills_df["Count"] > 0].sort_values("Count")
        st.plotly_chart(bar_h(top_s["Skill"].tolist(), top_s["Count"].tolist(), height=280),
                        use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="wcard"><div class="ctit">🏢 Work Model Distribution</div>', unsafe_allow_html=True)
        wm = filtered["On-site/Remote"].value_counts()
        wm = wm[wm.index != "Not Specified"]
        if len(wm) == 0:
            st.info("No data for current filter.")
        else:
            fig_wm = go.Figure(go.Pie(
                labels=wm.index, values=wm.values, hole=0.54,
                marker=dict(colors=[BLUE, BLUE_LIGHT, BLUE_PALE, GREY][:len(wm)],
                            line=dict(color='white', width=3)),
                textinfo='label+percent',
                textfont=dict(size=12, family="DM Sans"),
                hovertemplate="<b>%{label}</b><br>%{value} jobs (%{percent})<extra></extra>",
                pull=[0.04] + [0]*(len(wm)-1),
            ))
            fig_wm.update_layout(
                margin=dict(l=10, r=10, t=10, b=10), height=280,
                paper_bgcolor='white', showlegend=False,
                hoverlabel=dict(bgcolor="#0f2a6e", font_size=12, font_family="DM Sans"),
            )
            st.plotly_chart(fig_wm, use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="wcard"><div class="ctit">📊 Experience Level</div>', unsafe_allow_html=True)
        el = filtered["Experience Level"].value_counts()
        el = el[el.index != "Not Specified"]
        if len(el) == 0:
            st.info("No data for current filter.")
        else:
            mx = el.max()
            colors = [f"rgba(26,78,216,{0.40 + 0.60*(v/mx):.2f})" for v in el.values]
            st.plotly_chart(bar_v(el.index.tolist(), el.values.tolist(), colors=colors, height=280),
                            use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="gap-md"></div>', unsafe_allow_html=True)

    # Row 2
    c4, c5, c6 = st.columns(3, gap="small")
    with c4:
        st.markdown('<div class="wcard"><div class="ctit">📍 Jobs by City</div>', unsafe_allow_html=True)
        city_counts = filtered["Government"].value_counts().head(5).reset_index()
        city_counts.columns = ["City", "Count"]
        if city_counts.empty:
            st.info("No data.")
        else:
            fig_city = px.treemap(city_counts, path=["City"], values="Count", color="Count",
                color_continuous_scale=[[0,"#bfdbfe"],[0.4,"#3b82f6"],[1,"#1a4ed8"]])
            fig_city.update_traces(
                textinfo="label+value",
                textfont=dict(size=13, family="DM Sans"),
                hovertemplate="<b>%{label}</b><br>%{value} jobs<extra></extra>",
                marker=dict(pad=dict(t=20, l=6, r=6, b=6)),
            )
            fig_city.update_layout(
                margin=dict(l=0, r=0, t=6, b=0), height=230,
                paper_bgcolor='white', coloraxis_showscale=False,
                hoverlabel=dict(bgcolor="#0f2a6e", font_size=12, font_family="DM Sans"),
            )
            st.plotly_chart(fig_city, use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)

    with c5:
        st.markdown('<div class="wcard"><div class="ctit">📅 Experience Distribution</div>', unsafe_allow_html=True)
        exp_dist = filtered["Experience Years"].value_counts()
        exp_dist = exp_dist[exp_dist.index != "No Specific Yrs Of Exp"].head(6)
        if exp_dist.empty:
            st.info("No data.")
        else:
            fig_exp = bar_v(exp_dist.index.tolist(), exp_dist.values.tolist(), height=230)
            fig_exp.update_layout(xaxis=dict(tickfont=dict(size=10, color="#1e40af", family="DM Sans"), automargin=True))
            st.plotly_chart(fig_exp, use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)

    with c6:
        top_co = filtered["Company"].value_counts().head(6)
        rows = "".join([
            f'<div class="corow"><span class="con">{co}</span><span class="cob">{cnt} jobs</span></div>'
            for co, cnt in top_co.items()
        ]) if not top_co.empty else "<p style='color:#94a3b8;font-size:13px;padding:8px 0;'>No data.</p>"
        st.markdown(f'<div class="wcard"><div class="ctit">🏆 Top Hiring Companies</div>{rows}</div>',
                    unsafe_allow_html=True)

    st.markdown('<div class="gap-md"></div>', unsafe_allow_html=True)
    st.markdown("""<div class="ins"><div class="it">
        <strong>Key insight</strong> — Among jobs with a specified work model, on-site dominates at
        <strong>68%</strong>. Cairo and Giza hold <strong>91.4%</strong> of all data jobs.
        <strong>SQL</strong> and <strong>Business Analysis</strong> are the must-have skills.
    </div></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TAB 2
# ══════════════════════════════════════════════
with tab2:
    st.markdown('<div class="content-area">', unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4, gap="small")
    for col, lbl, val, sub in [
        (k1, "Data Jobs Share",     "8.3%",  "209 of 2,533 total listings"),
        (k2, "Remote Data Jobs",    "1.0%",  "vs 3.9% across all jobs"),
        (k3, "Entry Level Data",    "1.9%",  "vs 6.1% across all jobs"),
        (k4, "Cairo Concentration", "73.7%", "vs 66.1% across all jobs"),
    ]:
        with col:
            st.markdown(f"""<div class="kcard">
                <div class="klbl">{lbl}</div>
                <div class="kval">{val}</div>
                <div class="ksub">{sub}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div class="gap-md"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="small")
    with c1:
        st.markdown('<div class="wcard"><div class="ctit">🏢 Work Model Comparison</div>', unsafe_allow_html=True)
        st.plotly_chart(grouped_bar(["On-site","Hybrid","Remote"],
                                    [13.4,5.3,1.0],[24.6,8.2,3.9]),
                        use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="wcard"><div class="ctit">📊 Experience Level Comparison</div>', unsafe_allow_html=True)
        st.plotly_chart(grouped_bar(["Entry Level","Experienced","Manager"],
                                    [1.9,17.2,0.5],[6.1,27.4,2.8]),
                        use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="wcard"><div class="ctit">📍 City Concentration</div>', unsafe_allow_html=True)
        st.plotly_chart(grouped_bar(["Cairo","Giza","Alexandria"],
                                    [73.7,17.7,5.3],[66.1,20.0,7.1]),
                        use_container_width=True, config=PCFG)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="gap-md"></div>', unsafe_allow_html=True)
    st.markdown("""<div class="ins"><div class="it">
        <strong>Key finding</strong> — Data jobs are <strong>3× harder to enter</strong> than average —
        only <strong>1.9%</strong> entry-level vs 6.1% across all jobs.
        Also less remote-friendly (<strong>1% vs 3.9%</strong>) and more Cairo-concentrated.
    </div></div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)