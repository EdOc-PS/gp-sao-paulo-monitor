import { Link } from 'react-router-dom';

function Nav() {
    return (
        <>
            <div style={{
                width: "100%", height: 388, display: "flex", justifyContent: "end", backgroundColor: "#000",
                borderBottom: "1px solid #303037", flexDirection: "column", alignItems: "center"
            }}>
                <img src="https://media.formula1.com/image/upload/c_lfill,w_3392/q_auto/v1740000000/fom-website/manual/Misc/Red%20Box%20Image.webp" alt="" 
                    style={{ width: "50%", height: 310, objectFit: "cover", marginBottom: "1rem", borderRadius: 10}}/>
                <div style={{ width: "85%", padding: "0px 24px", backgroundColor: "#000", display: "flex", alignItems: "center" }}>
                    <p style={{ marginLeft: "26px" }} >2025</p>
                    <Link to='/cars' style={{ padding: "8px 24px" }}>Pilotos</Link>
                    <Link to='/dashboard' style={{ padding: "8px 24px" }}>Dashboard</Link>
                </div>
            </div>
        </>
    )
}

export default Nav