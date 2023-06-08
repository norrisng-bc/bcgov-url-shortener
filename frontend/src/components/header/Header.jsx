import './Header.css';
// import logo from '../../../public/BCID_H_rgb_rev.svg'
import logo from '/BCID_H_rgb_rev.svg'


const Header = () => {

  return (
    <header>
      <div className="banner">
        <a href="https://gov.bc.ca">
        <img src={logo} alt="Go to the Government of British Columbia website" />
        </a>
        <h1>URL Shortener</h1>
      </div>
      <div className="other">
          {/* This place is for anything that needs to be right aligned
          beside the logo. */}
        &nbsp;
      </div>
    </header>
  );
}

export default Header