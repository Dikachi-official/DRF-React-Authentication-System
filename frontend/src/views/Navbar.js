import React from "react"


function Navbar() {
    return (
        <div>
            <nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-dark">
                <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img style={{width:"80px", padding:"20px"}} src="https://i.imgur.com/juL1aAc.png" alt=""/>

                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Pricing</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled">Disabled</a>
                    </li>
                    </ul>
                </div>
                </div>
            </nav>
        </div>
    )
}

export default Navbar